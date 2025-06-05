# Creating Order Status Check Bot
This guide walks you through creating a practical example of implementing order status check functionality in your chatbot.

For a quick start, you can find a pre-configured bot in the examples folder. Import it through Settings/Data Management, then train the model via the "Train Models" button in the Intents page. Once done, you can proceed directly to the testing section.

## Configuration
### 1. Create Order Number Entity
1. Go to the Entities section
2. Create a new entity named "order_number"

![](/docs/screenshots/entities_configuration.png)

### 2 Create the Intent
1. Navigate to the Intents section in the admin interface
2. Click "Create Intent"
3. Configure the basic intent information:
    - Intent Name: "Check Order Status"
    - Intent ID: "check_order_status"

#### Configure Parameters

Add the following parameter:
- para 1
    - Name: "order_number"
    - Type: Select your order number entity type
    - Required: Yes
    - Prompt: "Please provide your order number"

- para 2 
    - Name: "order_number"
    - Type: Select your order number entity type

### 3. Set Up API Integration 
Configuration steps:
1. Enable "REST API Calling"
2. Add the API URL with parameter templating

``` 
https://fake-store-api.mock.beeceptor.com/api/orders/status?order_id={{ parameters['name'] }}
```
3. Choose method as GET
4. Leave the headers and JSON payload configurations as default

### 4. Configure Response Template
In the response section of the intent, customize the response using the API result:

```
Your order status is {{ result['status'] }}
-------------------------or--------------------------------
The total cost of the order is ${{ result['total_price'] }}
```

![](/docs/screenshots/intents_configuration.png)

## Training

Now, let's train the NLU models to understand the user queries. We support two types of NLU pipelines:

* Default NLU pipeline (using traditional ML and NLP algorithms, requires manual training)
* Zero Shot NLU pipeline (using LLMs, no manual training needed)
For this example, we'll use the default NLU pipeline.

### 1. Add Training Phrases
1. Go to Intents Page and click on the training icon
![](/docs/screenshots/training_icon.png)

2. Add the following example phrases
    - check my order
    - ORD123: $312
    - ORD456 is $789
    - ord178's order total is $1280 
    - other order total

### 2. Label Entities
1. In each training phrase, highlight the order numbers
2. Select the "order_number" and "price" entity type
3. Ensure all variations are properly labeled

![](/docs/screenshots/pos_intents_train.png)

### 3. Train the Model
1. Return to the Intents Page
2. Click "Train Models"
3. Wait for training completion
4. Test the intent with sample queries

## Testing
1. Navigate to the Chat Page
2. Test with different variations:
    - "Check my order total"
    - "ORD123"
3. Verify the following:
    - Intent is correctly identified
    - Order number is properly extracted
    - API is triggered with correct parameters
![](/docs/screenshots/testing.png)

## Next Stepts
`Coming soon`.