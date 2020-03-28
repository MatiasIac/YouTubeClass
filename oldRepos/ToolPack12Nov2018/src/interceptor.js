;(function(w){
    w.ToolPack = w.ToolPack || {};

    var interceptorPromise = function() {
        this._f = null;
        this._params = null;
        this._next = null;
        this._isSet = false;
    };

    interceptorPromise.prototype.having = function(f, params) {
        this._f = f;
        this._params = params || {
            'stopPropagation': false,
            'injectResult': false,
            'context': null
        };
        this._isSet = true;
        this._next = new interceptorPromise();
        return this._next;
    };

    var interceptor = function() {
        this._definitions = { };
    };

    interceptor.prototype._computeFunctionArgs = function(f) {
        var names = f.toString().match(/^[\s\(]*function[^(]*\(([^)]*)\)/)[1]
            .replace(/\/\/.*?[\r\n]|\/\*(?:.|[\r\n])*?\*\//g, '')
            .replace(/\s+/g, '').split(',');
        return names.length == 1 && !names[0] ? [] : names;
    };

    interceptor.prototype._bind = function(bindableObject, propertyName, injector) {
        var f = bindableObject[propertyName];
        bindableObject[propertyName] = function() {
            var interceptorResults = [];

            function navigate(navigator) {
                if (navigator === null) return;
                if (!navigator._isSet) return;
                var r = navigator._f.apply(navigator._params.context || bindableObject, arguments);
                
                if (navigator._params.stopPropagation === true && 
                    typeof(r) === 'boolean' &&
                    r === false) return;
                
                if (navigator._params.injectResult === true) {
                    interceptorResults.push(r);
                }
                
                navigate(navigator._next);
            }

            navigate(injector);

            var arg = Array.from(arguments);
            if (interceptorResults.length > 0) {
                arg = arg.concat(interceptorResults);
            }

            f.apply(bindableObject, arg);
        };
    };

    interceptor.prototype._computeProperties = function(o) {
        if (o === null) return;

        var names = Object.getOwnPropertyNames(o);
        if (names.length === 0) {
            this._computeProperties(Object.getPrototypeOf(o));
            return;
        }

        var n_length = names.length;
        for (var i = 0; i < n_length; i++) {
            var e = names[i];
            if (typeof Object.getOwnPropertyDescriptor(o, e).value === 'function') {
                var bindableArguments = this._computeFunctionArgs(Object.getOwnPropertyDescriptor(o, e).value);
                var interceptorName = bindableArguments.find(function(item) { 
                    return item.match(/^__/) !== null; 
                });

                if (interceptorName === undefined) continue;
                if (this._definitions[interceptorName] !== undefined) {
                    this._bind(o, e, this._definitions[interceptorName]);
                }
            }
        }
    };

    interceptor.prototype.define = function(injectorName) {
        var injectorDefinition = new interceptorPromise();
        this._definitions[injectorName] = injectorDefinition;
        return injectorDefinition;
    };

    interceptor.prototype.compute = function(injectable) {
        if (injectable === null) return;
        this._computeProperties(injectable);
    };

    w.ToolPack.Interceptor = new interceptor();
}(window));