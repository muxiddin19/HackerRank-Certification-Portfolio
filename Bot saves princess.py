displayPathtoPrincess() {
    local n=$1
    shift
    local grid=("$@")
    
    local bot_row=0
    local bot_col=0
    local princess_row=0
    local princess_col=0
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            if [[ "${grid[i]:$j:1}" == "m" ]]; then
                bot_row=$i
                bot_col=$j
            elif [[ "${grid[i]:$j:1}" == "p" ]]; then
                princess_row=$i
                princess_col=$j
            fi
        done
    done
    
    while [[ $bot_row -lt $princess_row ]]; do
        echo "DOWN"
        ((bot_row++))
    done
    
    while [[ $bot_row -gt $princess_row ]]; do
        echo "UP"
        ((bot_row--))
    done
    
    while [[ $bot_col -lt $princess_col ]]; do
        echo "RIGHT"
        ((bot_col++))
    done
    
    while [[ $bot_col -gt $princess_col ]]; do
        echo "LEFT"
        ((bot_col--))
    done
}

# Read grid size
read n

# Read grid
grid=()
for ((i=0; i<n; i++)); do
    read row
    grid+=("$row")
done

displayPathtoPrincess "$n" "${grid[@]}"
