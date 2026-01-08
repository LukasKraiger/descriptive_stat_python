library(readr)

df <- read_csv2("data_questionnaire.csv")

descriptive_statistics_r <- function(data) {
  numeric_data <- data[sapply(data, is.numeric)]
  
  results <- data.frame()
  
  for (col_name in names(numeric_data)) {
    clean_data <- na.omit(numeric_data[[col_name]])
    
    stats <- data.frame(
      Variable = col_name,
      Mean = mean(clean_data),
      Std_Deviation = sd(clean_data),
      Minimum = min(clean_data),
      Maximum = max(clean_data),
      Median = median(clean_data)
    )
    
    results <- rbind(results, stats)
  }
  
  return(results)
}

desc_stats_r <- descriptive_statistics_r(df)
print(desc_stats_r)