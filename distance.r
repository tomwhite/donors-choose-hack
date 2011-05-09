# Load the raw counts to do summary statistics
raw_data <- read.table("raw_counts.txt")
summary(raw_data)
png("distance-hist.png")
hist(raw_data$V1, breaks=200, xlab="Distance (miles)", ylab="Count", main="Histogram showing distance between project donors and schools")
dev.off()

# Load the bucketed data to draw scatter plots
data <- read.table("counts.txt")

png("distance-log.png")
plot(data, xlab="Distance (miles)", ylab="Log count", pch='.', log="y", main="Distance between project donors and schools (log y scale)")
dev.off()