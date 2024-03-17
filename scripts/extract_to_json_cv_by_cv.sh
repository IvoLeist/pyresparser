#!/bin/bash
# wraps pyresparser to extract cv by cv to json

copy_if_match() {
    local pattern=$1
    local dest_folder=$2
    local message=$3

    if grep -i -q -E "$pattern" "$output_dir/$filename.json"; then
        echo "$message"
        cp "$file" "$dest_folder"
    fi
}

# Change the IFS (Internal Field Separator) to handle newline only
IFS=$'\n'
input_dir="resumes/frontend/in"
output_dir="resumes/frontend/out/json"

find $input_dir -type f | while read -r file; do
    echo "Processing \"$file\""
    filename=$(basename -- "$file")
    filename="${filename%.*}"

    echo "Processing \"$filename\""
    echo "Output \"$output_dir/$filename.json\""
    # pyresparser -e json -f "$file" -o "$output_dir/$filename.json"

    copy_if_match "bootcamp" "resumes/frontend/filtered/bootcamp_participants" "copy \"$file\" to bootcamp folder"
    copy_if_match "(Master|M\.S\.)" "resumes/frontend/filtered/master_degree" "copy \"$file\" to master folder"
    copy_if_match "Computer Science" "resumes/frontend/filtered/computer_science_degree" "copy \"$file\" to computer science folder"
    copy_if_match "Senior" "resumes/frontend/filtered/senior" "copy \"$file\" to senior folder"
done

# Reset the IFS to its default value
unset IFS