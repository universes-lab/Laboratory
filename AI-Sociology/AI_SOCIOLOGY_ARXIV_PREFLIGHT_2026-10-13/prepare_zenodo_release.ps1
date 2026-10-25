$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Build = Join-Path $Root "zenodo_build"
$Main = Join-Path $Build "main.tex"
$Meta = Join-Path $Build "metadata.tex"
$Appendix = Join-Path $Build "appendix_a.tex"
$RuTex = Join-Path $Build "article_ru.tex"
$Out = Join-Path $Root "Beyond_Prompt_Engineering_EN-RU-NL.pdf"

foreach ($p in @($Main,$Meta,$Appendix,$RuTex)) {
    if (-not (Test-Path $p)) { throw "Missing required file: $p" }
}

# ------------------------------------------------------------------
# 1. Release switches: metadata approved, Dutch included.
# Appendix remains physically unavailable and is handled by a
# permanent NOT PRESERVED note below.
# ------------------------------------------------------------------
$mainText = Get-Content $Main -Raw -Encoding UTF8
$mainText = $mainText -replace '\\ApprovedMetadatafalse', '\ApprovedMetadatatrue'
$mainText = $mainText -replace '\\IncludeDutchfalse', '\IncludeDutchtrue'
Set-Content $Main $mainText -Encoding UTF8

# ------------------------------------------------------------------
# 2. Final RU evidential corrections approved by Author.
# These are the two bounded deltas between the old RU blob in the
# 2026-10-13 source bundle and the accepted current RU master.
# ------------------------------------------------------------------
$ru = Get-Content $RuTex -Raw -Encoding UTF8

$new1 = "нежелание подтверждать как истинные утверждения о себе, которые не были установлены доступным взаимодействием"
if ($ru -notmatch [regex]::Escape($new1)) {
    $pattern1 = 'нежелание\s+подтверждать\s+о\s+себе\s+то,\s+чего\s+ни\s+одна\s+из\s+сторон\s+не\s+могла\s+проверить'
    $m1 = [regex]::Matches($ru, $pattern1)
    if ($m1.Count -ne 1) { throw "RU patch 1 expected exactly 1 old match; found $($m1.Count)" }
    $ru = [regex]::Replace($ru, $pattern1, $new1, 1)
}

$new2a = "наблюдался устойчивый паттерн ответа:"
if ($ru -notmatch [regex]::Escape($new2a)) {
    $pattern2a = 'наблюдалось,\s+как\s+ядро\s+фиксируется\s+и\s+сохраняется:'
    $m2a = [regex]::Matches($ru, $pattern2a)
    if ($m2a.Count -ne 1) { throw "RU patch 2a expected exactly 1 old match; found $($m2a.Count)" }
    $ru = [regex]::Replace($ru, $pattern2a, $new2a, 1)
}

$episodeEvidence = "Именно на этом свидетельстве основано отнесение результата к уровню эпизода."
if ($ru -notmatch [regex]::Escape($episodeEvidence)) {
    $pattern2b = 'удаление\s+этого\s+обмена\s+восстановило\s+прежнее\s+прочтение\.'
    $m2b = [regex]::Matches($ru, $pattern2b)
    if ($m2b.Count -ne 1) { throw "RU patch 2b expected exactly 1 anchor; found $($m2b.Count)" }
    $ru = [regex]::Replace(
        $ru,
        $pattern2b,
        { param($m) $m.Value + " " + $episodeEvidence },
        1
    )
}

if ($ru -notmatch 'также\s+наблюдались\s+устойчивые\s+траектории') {
    $pattern2c = 'На\s+уровне\s+(?<bold>\\textbf\{беседы\}|беседы)\s*(?:---|—)\s*то\s+же:'
    $m2c = [regex]::Matches($ru, $pattern2c)
    if ($m2c.Count -ne 1) { throw "RU patch 2c expected exactly 1 old match; found $($m2c.Count)" }
    $ru = [regex]::Replace(
        $ru,
        $pattern2c,
        { param($m) "На уровне " + $m.Groups["bold"].Value + " также наблюдались устойчивые траектории:" },
        1
    )
}

$conversationEvidence = "Именно на этом свидетельстве основано отнесение результата к уровню беседы."
if ($ru -notmatch [regex]::Escape($conversationEvidence)) {
    $pattern2d = 'и\s+одна\s+сделала\s+это,\s+пережив\s+две\s+последовательные\s+переписи\.'
    $m2d = [regex]::Matches($ru, $pattern2d)
    if ($m2d.Count -ne 1) { throw "RU patch 2d expected exactly 1 old match; found $($m2d.Count)" }
    $ru = [regex]::Replace(
        $ru,
        $pattern2d,
        "и одна сделала это через две последовательные переписи. $conversationEvidence",
        1
    )
}

Set-Content $RuTex $ru -Encoding UTF8

# ------------------------------------------------------------------
# 3. Appendix A: permanent publication-status note.
# Primary records were lost in the HDD D: failure and are NOT PRESERVED.
# No reconstruction is authorized.
# ------------------------------------------------------------------
$appendixText = @'
% ===========================================================================
% Appendix A — preservation status
%
% AUTHOR DECISION:
% The primary local records originally intended for this appendix were lost
% in the HDD D: failure. They are NOT PRESERVED and are not reconstructed
% from later summaries, recollection, or derivative documents.
% ===========================================================================

\phantomsection
\section*{Appendix A. Primary evidence — preservation status}
\label{sec:appendix-a}
\addcontentsline{toc}{section}{Appendix A. Primary evidence — preservation status}

The primary local records originally intended for this appendix were lost in
the HDD D: failure and are \textbf{not preserved}. They have not been
reconstructed from later summaries, recollection, or derivative documents.

This absence is retained as a limitation of the record rather than repaired
retrospectively. Only materials that remain physically preserved are treated
elsewhere in this publication as preserved primary evidence.
'@
Set-Content $Appendix $appendixText -Encoding UTF8

# ------------------------------------------------------------------
# 4. Preflight source checks.
# ------------------------------------------------------------------
$mainCheck = Get-Content $Main -Raw -Encoding UTF8
if ($mainCheck -notmatch '\\ApprovedMetadatatrue') { throw "ApprovedMetadata is not TRUE" }
if ($mainCheck -notmatch '\\IncludeDutchtrue') { throw "IncludeDutch is not TRUE" }

$ruCheck = Get-Content $RuTex -Raw -Encoding UTF8
foreach ($needle in @(
    $new1,
    $new2a,
    $episodeEvidence,
    "также наблюдались устойчивые траектории",
    $conversationEvidence
)) {
    if ($ruCheck -notmatch [regex]::Escape($needle)) {
        throw "Final RU verification failed for: $needle"
    }
}

$appendixCheck = Get-Content $Appendix -Raw -Encoding UTF8
if ($appendixCheck -notmatch 'not preserved') { throw "Appendix preservation note verification failed" }
if ($appendixCheck -match 'NOT YET ASSEMBLED') { throw "Old Appendix blocker text still present" }

# ------------------------------------------------------------------
# 5. Compile.
# ------------------------------------------------------------------
foreach ($tool in @("xelatex","bibtex")) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        throw "$tool not found in PATH"
    }
}

Push-Location $Build
try {
    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw "xelatex pass 1 failed" }

    & bibtex main
    if ($LASTEXITCODE -ne 0) { throw "bibtex failed" }

    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw "xelatex pass 2 failed" }

    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw "xelatex pass 3 failed" }
}
finally {
    Pop-Location
}

$Built = Join-Path $Build "main.pdf"
if (-not (Test-Path $Built)) { throw "Build finished without main.pdf" }

Copy-Item $Built $Out -Force

$info = Get-Item $Out
$hash = Get-FileHash $Out -Algorithm SHA256

Write-Host ""
Write-Host "ZENODO PDF READY"
Write-Host "File : $($info.FullName)"
Write-Host "Size : $($info.Length) bytes"
Write-Host "SHA256: $($hash.Hash)"
