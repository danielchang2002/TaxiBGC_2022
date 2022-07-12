FNR == 1   { for(i = 1; i <= NF; i++) a[i] = $i;  next }
$1 == a[1] { for(i = 2; i <= NF; i++) a[i] += $i; next }
{
    printf "%s", a[1]; a[1] = $1;
    for(i = 2; i <= NF; i++) { printf "\t%s", a[i]; a[i] = $i };
    printf "\n";
}
END {
    printf "%s", a[1];
    for(i = 2; i <= NF; i++) printf "\t%s", a[i];
    printf "\n";
}
