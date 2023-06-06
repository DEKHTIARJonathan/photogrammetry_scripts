IMG_QUALITIES=(
  "50"
  "60"
  "70"
  "80"
  "85"
  "90"
  "95"
  "99"
  "100"
)


for quality in "${IMG_QUALITIES[@]}"; do
    echo "============= Compression ${quality}% ============="
    sleep 2
    OUTPUT_FOLDER_NAME="JPEG_${quality}"
    rm -rf "${OUTPUT_FOLDER_NAME}"
    mkdir -p "${OUTPUT_FOLDER_NAME}/TIFF"
    find TIFF -type f -name "*.tif" | xargs -I {} mogrify -format jpeg -verbose -output-directory "${OUTPUT_FOLDER_NAME}/" -quality "${quality}" {}
    mv ./${OUTPUT_FOLDER_NAME}/TIFF/*.jpeg ./${OUTPUT_FOLDER_NAME}
    rmdir "${OUTPUT_FOLDER_NAME}/TIFF"
done

du -h | sort -h
