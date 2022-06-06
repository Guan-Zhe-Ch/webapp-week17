if (test-path main.js) {
        py -3 .check/checks.py $args[0]
} else {
    Write-Output "`nmain.js: No such file!`n"
}

