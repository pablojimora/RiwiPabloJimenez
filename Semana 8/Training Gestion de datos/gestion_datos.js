// Project Initialization
console.log("Data Management with Objects, Sets, and Maps!");

const products = {
    1: {id: 1, name: "Laptop", price: 1500},
    2: {id: 2, name: "Mouse", price: 25},
    3: {id: 3, name: "Keyboard", price: 50}  
};

//console.log("Products object: ", products);

// Create a Set with product names
const productSet = new Set(Object.values(products).map(product => product.name));
//console.log("Set of unique products: ", productSet);

// Create a Map to add categories to products
//I organized the map in a different way to training so that it could read all the data and not be affected by the same keys
const mapProduct = new Map([
    ["Laptop", "Electronics"],
    ["Mouse", "Accessories"],
    ["Keyboard", "Accessories"],
]);

//console.log("Map of product categories: ", mapProduct);
console.log("Object Products")
// Loop through the products object
for (const id in products) {
    console.log(`Product ID: ${id}, Details: `, products[id]);
}
console.log(" ")
console.log("Set of unique products: ")
// Loop through the Set using for...of
for (const product of productSet) {
    console.log("Unique product:", product);
}
console.log(" ")
console.log("Products and categories   ")
// Loop through the Map of products
mapProduct.forEach((category, product ) => {
    console.log(`Category: ${category}, Product: ${product}`);
});  




