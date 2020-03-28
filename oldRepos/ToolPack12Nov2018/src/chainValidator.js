;(function(w){
    w.ToolPack = w.ToolPack || {};

    var chain = function (func) {
        this._enabled = true;
        this._callback = func;
    };

    Object.defineProperty(chain.prototype, "enabled", {
        set: function (enabled) {
            this._enabled = enabled === true;
        },
        get: function () { 
            return this._enabled;
        }
    });

    var validationResult = function () {
        this._errors = [];
    };

    Object.defineProperty(validationResult.prototype, "isValid", { 
        get: function () { 
            return this._errors.length === 0;
        }
    });

    Object.defineProperty(validationResult.prototype, "errors", { 
        get: function () { 
            return this._errors;
        }
    });

    validationResult.prototype.addError = function (message) {
        this._errors.push(message);
    };

    var validator = function (stopOnError) { 
        this._definitions = [];
        this._stopOnError = stopOnError || true;
    };

    validator.prototype.define = function (func) {
        this._definitions.push(new chain(func));
        return this;
    };

    validator.prototype.validate = function (data) {
        var self = this;
        var result = new validationResult();
        var chainLength = this._definitions.length;

        for (var i = 0; i < chainLength; i++) {
            var currentChain = this._definitions[i];
            if (!currentChain.enabled) continue;

            try {
                var functionOutput = currentChain._callback(data);

                if (typeof(functionOutput) !== 'undefined') {
                    result.addError(typeof(functionOutput.message) !== 'undefined' ? 
                        functionOutput.message : 
                        functionOutput);
                    if (self._stopOnError) break;
                }
            } catch (error) {
                result.addError(error);
                if (self._stopOnError) break;
            }
        }

        return result;
    };
    
    w.ToolPack.ChainValidator = validator;
}(window));