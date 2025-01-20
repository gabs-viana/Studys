function Get-FileSHA1($filePath) {
    # Lê o arquivo diretamente como bytes
    $fileBytes = [System.IO.File]::ReadAllBytes($filePath)
    $sha1 = New-Object System.Security.Cryptography.SHA1Managed
    $hash = $sha1.ComputeHash($fileBytes)

    $prettyHashSB = New-Object System.Text.StringBuilder
    foreach ($byte in $hash) {
        $hexaNotation = $byte.ToString("X2")
        $prettyHashSB.Append($hexaNotation)
    }

    Write-Host $prettyHashSB.ToString() -BackgroundColor Black -ForegroundColor Green 
}


Get-FileSHA1 "C:\Users\gabriel.viana\OneDrive - CONASA INFRAESTRUTURA S.A\GabsDev\GitHub\GabsStudys\Scripts\ShaFile.ps1"

function Get-FileSHA256(){

}

function Get-FileSHA384(){

}

function Get-FileSHA512(){

}