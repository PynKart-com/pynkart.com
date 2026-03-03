# PowerShell script to convert SVG to PNG for Odoo
# This script uses Windows COM objects to convert SVG to PNG

Write-Host "=== PynKart ZPL Studio - SVG to PNG Converter ===" -ForegroundColor Cyan
Write-Host ""

# Check if Chrome or Edge is installed (for headless conversion)
$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if (-not (Test-Path $chromePath) -and -not (Test-Path $edgePath)) {
    Write-Host "ERROR: Chrome or Edge browser is required for SVG to PNG conversion" -ForegroundColor Red
    Write-Host ""
    Write-Host "MANUAL CONVERSION STEPS:" -ForegroundColor Yellow
    Write-Host "1. Open icon.svg in a web browser"
    Write-Host "2. Right-click > Inspect Element > Console"
    Write-Host "3. Paste this code:"
    Write-Host ""
    Write-Host @"
const svg = document.querySelector('svg');
const canvas = document.createElement('canvas');
canvas.width = 256;
canvas.height = 256;
const ctx = canvas.getContext('2d');
const data = new XMLSerializer().serializeToString(svg);
const img = new Image();
img.onload = () => {
    ctx.drawImage(img, 0, 0);
    const a = document.createElement('a');
    a.download = 'icon.png';
    a.href = canvas.toDataURL('image/png');
    a.click();
};
img.src = 'data:image/svg+xml;base64,' + btoa(data);
"@ -ForegroundColor Green
    Write-Host ""
    Write-Host "4. Repeat for banner.svg (1200x400) and save as banner.png"
    Write-Host ""
    Write-Host "ALTERNATIVE: Use online converter at https://cloudconvert.com/svg-to-png" -ForegroundColor Yellow
    exit
}

# Use Chrome/Edge to convert SVG to PNG
$browser = if (Test-Path $chromePath) { $chromePath } else { $edgePath }

Write-Host "Using browser: $browser" -ForegroundColor Green
Write-Host ""

# Function to convert SVG to PNG
function Convert-SvgToPng {
    param(
        [string]$svgFile,
        [string]$pngFile,
        [int]$width,
        [int]$height
    )
    
    Write-Host "Converting $svgFile -> $pngFile ($width x $height)" -ForegroundColor Yellow
    
    # Create HTML wrapper
    $html = @"
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>body{margin:0;padding:0;}</style>
</head>
<body>
    <img id="img" src="$svgFile" style="width:${width}px;height:${height}px;">
    <script>
        setTimeout(() => {
            const img = document.getElementById('img');
            const canvas = document.createElement('canvas');
            canvas.width = $width;
            canvas.height = $height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, $width, $height);
            canvas.toBlob(blob => {
                const a = document.createElement('a');
                a.download = '$pngFile';
                a.href = URL.createObjectURL(blob);
                a.click();
            }, 'image/png');
        }, 1000);
    </script>
</body>
</html>
"@
    
    $tempHtml = [System.IO.Path]::GetTempFileName() + ".html"
    $html | Out-File -FilePath $tempHtml -Encoding UTF8
    
    # Open in headless browser
    Start-Process $browser -ArgumentList "--headless", "--screenshot=$pngFile", "--window-size=$width,$height", $tempHtml -Wait
    
    Remove-Item $tempHtml -Force
    
    if (Test-Path $pngFile) {
        Write-Host "  ✓ Created $pngFile" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Failed to create $pngFile" -ForegroundColor Red
    }
}

# Convert icon.svg to icon.png (256x256)
Convert-SvgToPng -svgFile "icon.svg" -pngFile "icon.png" -width 256 -height 256

# Convert banner.svg to banner.png (1200x400) for cover image
Convert-SvgToPng -svgFile "banner.svg" -pngFile "banner.png" -width 1200 -height 400

Write-Host ""
Write-Host "=== Conversion Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Verify icon.png is 256x256 pixels"
Write-Host "2. Verify banner.png is 1200x400 pixels"
Write-Host "3. Create 3 screenshots: screenshot_1.png, screenshot_2.png, screenshot_3.png"
Write-Host "4. Update __manifest__.py images list"
Write-Host ""
