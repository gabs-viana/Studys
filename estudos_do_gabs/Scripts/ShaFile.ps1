function Get-FileSHA1($filePath){
    $fileContent = Get-Content $filePath
    $fileBytes = [System.Text.Encoding]::UTF8.GetBytes($fileContent)
    $sha1 = New-Object System.Security.Cryptography.SHA1Managed
    $hash = $sha1.ComputeHash($fileBytes)
    Write-Host $hash -BackgroundColor Black -ForegroundColor Green 
}

Get-FileSHA1 D:\Gabs\Gab-Dev\estudos_do_gabs\estudos_do_gabs\Scripts\ShaFile.ps1

function Get-FileSHA256(){

}

function Get-FileSHA384(){

}

function Get-FileSHA512(){

}