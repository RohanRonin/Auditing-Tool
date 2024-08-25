# Example: Check if Windows Firewall is enabled
$firewallStatus = Get-NetFirewallProfile -Profile Domain,Public,Private | Select-Object -Property Name, Enabled
$status = $true

foreach ($fw in $firewallStatus) {
    if ($fw.Enabled -eq 0) {
        $status = $false
    }
}

if ($status) {
    Write-Output "Firewall is enabled and the system is safe."
} else {
    Write-Output "Firewall is disabled and the system is not safe."
}
