# Paper Hearts Recommendation Database

### Data Model

| Table Name        | Description                         |
|-------------------|-------------------------------------|
| `customers_data`       | Stores customer details             |
| `transactions_data`    | Records transaction details         |
| `items_data`           | Contains item information           |
| `depositdata_data`  | Stores deposit information |
| `payments_data`  | Records payment details |


# Customers_Data
| Column Name        | Description                         |
|-------------------|-------------------------------------|
| `Customer ID`       | Unique Customer Identifier          |
| `Customer Name`    | Optional Customer Name         |


# Transactions_Data
| Column Name        | Description                         |
|-------------------|-------------------------------------|
| `Date`       | Date of transaction             |
| `Time`    | Time of transaction         |
| `Qty`           | Number of items in transaction           |
| `Discounts`  | Optional Discounts |
| `Net Sales`  | Net Sales of Transaction |
| `Tax`       | Taxes Collected             |
| `Transaction ID`    | Unique Transaction Identifier         |
| `Payment ID`           | Unique Payment Identifier           |
| `Device Name`  | POS Name |
| `Notes`  | Item description |
| `Details`       | Link to Square Transaction             |
| `Event Type`    | Type of Transaction         |
| `Customer ID`           | Unique Customer Identifier           |
| `Unit`  | Type of Quantity (i.e. ea) |
| `Count`  | Number of items in transaction |
| `Itemization`       | Type of items sold (i.e. Physical Good)             |
| `Employee`    | Name of Employee completing transaction         |
| `Token`           | Unique Item Identifier           |

# Items_Data
| Column Name        | Description                         |
|-------------------|-------------------------------------|
| `Token`       | Unique Item Identifier             |
| `Category`    | Type of Item         |
| `Item`           | Item Name           |
| `Price Point Name`  | Pricing Type |
| `SKU`  | Optional Item Identifier |
| `Gross Sales`  | Standard Price |

# DepositData_Data
| Column Name        | Description                         |
|-------------------|-------------------------------------|
| `Deposit ID`       | Unique Deposit Identifier             |
| `Deposit Date`    | Date of Deposit         |
| `Deposit Details`           | Link to Square Deposit           |


# Payments_Data
| Column Name        | Description                         |
|-------------------|-------------------------------------|
| `Payment ID`       | Unique Payment Identifier             |
| `Card Brand`    | Card Type (i.e. MasterCard)         |
| `PAN Suffix`           | Last 4 of CC Number           |
| `Gross Sales`  | Total Sales |
| `Discounts`  | Total Discounts |
| `Service Charges`       | Total Service Charges             |
| `Net Sales`    | Net Sales (Gross Sales - Discounts)         |
| `Gift Card Sales`           | Total Gift Card Sales           |
| `Tax`  | Taxes Collected |
| `Tip`  | Tip Collected |
| `Total Collected`       | Total Collected by Business             |
| `Source`    | Type of Payment         |
| `Card`           | Total Charged to Card           |
| `Card Entry Methods`  | Card Interactions |
| `Cash`  | Total Cash Collected |
| `Square Gift Card`       | Total Collected from Gift Cards             |
| `Other Tender`    | Total Collected from Other Tender         |
| `Other Tender Type`    | Type of Other Tender         |
| `Other Tender Note`           | Optional Note on Other Tender           |
| `Fees`  | Fees Charged by Square |
| `Fee Percentage Rate`  | Fee Rate Charged by Square |
| `Fee Fixed Rate`       | Fee Charged by Square             |
| `Cash App`    | Monies Received through CashApp         |
| `Refund Reason`           | Refund Processing Reason           |
| `Discount Name`  | Name of Discount Provided |
| `Event Type`  | Transaction Type |