# RBG Skin Confidence Dataset Generator

## Scripts
- `generate_image.py`: Generates all possible RBG files into 256 files
- `read_generated_image.py`: Generates output dataset for RBG confidence in
format `{r,g,b} {confidence}` where confidence is a int from 0 (least confident)
to 255 (most confident)

## Folders
- `images`: All possible RBG images
- `scoremap`: Output of running local R model (in jpg form)
- `db_table`: Output of the confidence dataset. Can be consumed locally
or updated to remote NoSQL table

## Running the R Model

- `Rscript Test_Pascal_Skin.R` where `Test_Pascal_Skin.R` is modified to
where the input images and output scoremaps need to be


test change
