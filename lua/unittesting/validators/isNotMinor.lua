function IsUserMinor()
    local age = IdentityService:GetUserAge()
    return age <= 18
end