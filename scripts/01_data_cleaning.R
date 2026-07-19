library(tidyverse)

# Read data
df <- read.csv("data/AP Research 25-26 - Sheet1.csv")

cat("\n===== Original Data =====\n")
print(head(df))

cat("\n===== Structure =====\n")
str(df)

cat("\n===== Missing Values =====\n")
print(colSums(is.na(df)))

cat("\n===== Duplicate Rows =====\n")
print(sum(duplicated(df)))

# Rename columns
colnames(df) <- c(
  "Concentration",
  "Ectopic_Vulva",
  "MUV"
)

# Clean concentration
df$Concentration <- gsub("[^0-9]", "", df$Concentration)
df$Concentration <- as.numeric(df$Concentration)

# Convert MUV
df$MUV <- ifelse(df$MUV == "Yes", 1, 0)

cat("\n===== Cleaned Data =====\n")
print(head(df))

cat("\n===== Summary =====\n")
summary(df)

write.csv(
  df,
  "results/cleaned_dataset.csv",
  row.names = FALSE
)

cat("\nCleaned dataset saved to results/cleaned_dataset.csv\n")
