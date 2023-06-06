#! /usr/bin/bash

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

DATASETS=(
  "50FT CW bs"
  "GIANT_SLOTH"
)

OUTPUT_FORMATS=(
   "PNG"
   "WEBP"
   "JPEG"
   "TIFF"
)

for ds_name in "${DATASETS[@]}"; do
    echo "[*] Processing Dataset: \`${ds_name}\` ..."
    for output_format in "${OUTPUT_FORMATS[@]}"; do
      for compression_lvl in "${IMG_QUALITIES[@]}"; do
          echo "    - [${output_format}] Compression Level: ${compression_lvl} ..."
          python3 batch_convert.py \
            --source_dir="${ds_name}/JPEG_100" \
            --destination_dir="${ds_name}/${output_format}_${compression_lvl}" \
            --output_format=${output_format} \
            --compression_lvl=${compression_lvl}
      done
    done
    echo
done
