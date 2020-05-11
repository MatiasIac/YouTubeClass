mockObject = { }
mockObject.__index = mockObject

function mockObject:new()
    local obj = { }
    setmetatable(obj, mockObject)
    obj.attributes = { }
    return obj
end

function mockObject:GetAttribute(name)
    return self.attributes[name]
end

function mockObject:SetAttribute(name, value)
    self.attributes[name] = value
end