#!/bin/bash
# wraps pyresparser to extract cv by cv to json

# Function to remove text with ANSI color codes
remove_colored_text() {
    sed 's/\x1b\[[0-9;]*m[^[:cntrl:]]*\x1b\[00m//g'
}

# Change the IFS (Internal Field Separator) to handle newline only
IFS=$'\n'
input_dir="resumes/frontend/in"
output_dir="resumes/frontend/out/json"

# reset jq_parse_errors.csv
echo "filename;error" > $output_dir/invalid/jq_parse_errors.csv

find $input_dir -type f | while read -r file; do
    echo "Processing \"$file\""
    filename=$(basename -- "$file")
    filename="${filename%.*}"

    echo "Processing \"$filename\""
    echo "Output \"$output_dir/$filename.json\""
    res=$(pyresparser -f "$file")
    cleaned_res=$(echo $res | remove_colored_text)
    output_fn="$filename".json

    if error_message=$(echo "$cleaned_res" | jq . 2>&1 >/dev/null); then
        echo "Valid JSON. Writing to file..."
        echo $cleaned_res > $output_dir/valid/$output_fn
    else
        invalid_out_dir=$output_dir/invalid
        echo "Invalid JSON. Storing error..."
        echo "$output_fn;$error_message" >> $invalid_out_dir/jq_parse_errors.csv
        echo $cleaned_res > $invalid_out_dir/$output_fn
    fi
    break
done

# Reset the IFS to its default value
unset IFS