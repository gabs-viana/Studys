Connect-MgGraph

# Get Service Principal using objectId
$sp = Get-MgServicePrincipal -ServicePrincipalId d2f495af-f666-471b-9239-723b19b4f74d

# Get MS Graph App role assignments using objectId of the Service Principal
$assignments = Get-MgServicePrincipalAppRoleAssignedTo -ServicePrincipalId $sp.Id -All | Where-Object {$_.PrincipalType -eq "User"}

# Revoke refresh token for all users assigned to the application
$assignments | ForEach-Object {
    Invoke-MgInvalidateUserRefreshToken -UserId $_.PrincipalId
}