local luaUnit = require('../unittest/luaunit')
require('../unittest/mocks')
require('../validators/isNotMinor')

function mockObject:GetUserAge()
    return self.attributes['age']
end

IdentityService = mockObject:new()

function DoTest(age, expected)
    IdentityService:SetAttribute('age', age)
    local result = IsUserMinor()
    luaUnit.assertEquals(result, expected)
end

DoTest(10, true)