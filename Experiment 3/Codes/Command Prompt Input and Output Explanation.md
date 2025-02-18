<div style='text-align:center; color: #00B050'>
<h1 style="font-size: 16pt">Author: Madhurima Rawat</h1>
<h2 style="font-size: 14pt"> Working with Cloud Storage Services</h2>

<h3 style="font-size: 12pt">This experiment demonstrates setting up an AWS S3 bucket, uploading and retrieving data, and verifying storage. It ensures scalable and secure cloud-based data management. The guide covers configuration, transfers, and retrieval steps.</h3>
</div>

---

## **1. Listing S3 Buckets**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566 --region us-east-1 s3 ls
```

### **Explanation:**

- `aws s3 ls` → Lists all available S3 buckets.
- `--endpoint-url=http://localhost:4566` → Specifies the LocalStack endpoint for simulating AWS S3.
- `--region us-east-1` → Defines the AWS region.

### **Output:**

```
(No output initially, as no buckets exist.)
```

### **Breakdown of Output:**

- _(No buckets found initially.)_
- Once a bucket is created, it will appear in the list.

---

## **2. Creating an S3 Bucket**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566
--region us-east-1 s3 mb s3://my-test-bucket
```

### **Explanation:**

- `aws s3 mb s3://my-test-bucket` → Creates a new S3 bucket named `my-test-bucket`.
- `--endpoint-url=http://localhost:4566` → Uses LocalStack to simulate AWS.
- `--region us-east-1` → Specifies the AWS region.

### **Output:**

```
make_bucket: my-test-bucket
```

### **Breakdown of Output:**

- `make_bucket: my-test-bucket` → Confirms that the bucket `my-test-bucket` was successfully created.

---

## **3. Listing S3 Buckets Again**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566 --region us-east-1 s3 ls
```

### **Explanation:**

- Lists all available S3 buckets in LocalStack.

### **Output:**

```
2025-02-18 10:55:33 my-test-bucket
```

### **Breakdown of Output:**

- `2025-02-18 10:55:33` → Timestamp when the bucket was created.
- `my-test-bucket` → Name of the newly created bucket.

---

## **4. Uploading Files to S3**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566 --region us-east-1 s3 cp . s3://my-test-bucket/ --recursive
```

### **Explanation:**

- `aws s3 cp . s3://my-test-bucket/ --recursive` → Uploads all files from the current directory to `my-test-bucket`.
- `--recursive` → Ensures all files in the folder are uploaded.

### **Output:**

```
upload: .\Sample_Housing_CSV_File.csv to
s3://my-test-bucket/Sample_Housing_CSV_File.csv
upload: .\storage_service_offered_by_amazon.png to
s3://my-test-bucket/storage_service_offered_by_amazon.png
upload: .\Data_Transfer_Amazon.jpg to
s3://my-test-bucket/Data_Transfer_Amazon.jpg
```

### **Breakdown of Output:**

- Each `upload:` line indicates a file being successfully uploaded.
- Shows the source file location and the target S3 bucket location.

---

## **5. Listing Uploaded Files in S3**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566
--region us-east-1 s3 ls s3://my-test-bucket/
```

### **Explanation:**

- `aws s3 ls s3://my-test-bucket/` → Lists all files inside `my-test-bucket`.

### **Output:**

```
2025-02-18 11:23:34      89553 Data_Transfer_Amazon.jpg
2025-02-18 11:23:34      29981 Sample_Housing_CSV_File.csv
2025-02-18 11:23:34      47575 storage_service_offered_by_amazon.png
```

### **Breakdown of Output:**

- `2025-02-18 11:23:34` → Timestamp of the file upload.
- `89553` → Size of the file `Data_Transfer_Amazon.jpg` in bytes.
- `29981` → Size of `Sample_Housing_CSV_File.csv` in bytes.
- `47575` → Size of `storage_service_offered_by_amazon.png` in bytes.

---

## **6. Downloading a File from S3**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566
--region us-east-1 s3 cp s3://my-test-bucket/Sample_Housing_CSV_File.csv .
```

### **Explanation:**

- Downloads `Sample_Housing_CSV_File.csv` from `my-test-bucket` to the current directory.

### **Output:**

```
download: s3://my-test-bucket/Sample_Housing_CSV_File.csv
to .\Sample_Housing_CSV_File.csv
```

### **Breakdown of Output:**

- `download:` → Confirms that the file was successfully retrieved.
- Shows source (S3 bucket) and destination (local directory).

---

## **7. Viewing the Downloaded CSV File**

### **Command:**

```sh
type Sample_Housing_CSV_File.csv
```

### **Explanation:**

- Displays the content of the CSV file.

### **Output:**

```
price,area,bedrooms,bathrooms,stories,mainroad,guestroom,
basement,hotwaterheating,airconditioning,parking,
prefarea,furnishingstatus
13300000,7420,4,2,3,yes,no,no,no,yes,2,yes,furnished
12250000,8960,4,4,4,yes,no,no,no,yes,3,no,furnished
...
```

### **Breakdown of Output:**

- Displays data from the CSV file in tabular format.
- Column names are listed first, followed by property data.

---

## **8. Opening an Image File**

### **Command:**

```sh
start Data_Transfer_Amazon.jpg
```

### **Explanation:**

- Opens the image file using the default image viewer.

### **Output:**

_(Image opens in the default viewer.)_

---

## **9. Opening Another Image File**

### **Command:**

```sh
start storage_service_offered_by_amazon.png
```

### **Explanation:**

- Opens another image file.

### **Output:**

_(Image opens in the default viewer.)_

---

## **10. Downloading a File to a Specific Location**

### **Command:**

```sh
aws --endpoint-url=http://localhost:4566 --region
us-east-1 s3 cp s3://my-test-bucket/Sample_Housing_CSV_File.csv
"C:\Users\rawat\Downloads\Sample_Housing_CSV_File.csv"
```

### **Explanation:**

- Downloads `Sample_Housing_CSV_File.csv` and saves it to the `Downloads` folder.

### **Output:**

```
download: s3://my-test-bucket/Sample_Housing_CSV_File.csv
to ..\..\..\..\..\..\Downloads\Sample_Housing_CSV_File.csv
```

### **Breakdown of Output:**

- `download:` → Confirms successful file retrieval.
- Source (S3 bucket) and destination (local `Downloads` folder) are displayed.
