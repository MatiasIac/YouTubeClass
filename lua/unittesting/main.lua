require('objects/identity')
require('validators/isNotMinor')

local isMinor = IsUserMinor()

if isMinor then
    print('User is minor')
else
    print('User is not minor')
end