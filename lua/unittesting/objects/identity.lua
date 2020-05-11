local Identity = { }
Identity.__index = Identity

function Identity:new()
    local idt = {}
    setmetatable(idt, Identity)
    return idt
end

function Identity:GetUserAge()
    return 20
end

IdentityService = Identity:new()