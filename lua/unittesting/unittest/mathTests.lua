local luaUnit = require('../unittest/luaunit')
require('../functions/math')

function DoTest(valA, valB, expected)
    local result = suma(valA, valB)
    luaUnit.assertEquals(result, expected)
end

function When_SumValues_Expect_Results()
    DoTest(10, 10, 20)
end

When_SumValues_Expect_Results()