var createCounter = function(n) {
	let num = n;

	let count = num;
	return function() {
		console.log(count);
		return count++;
	};

}
const counter = createCounter(10)
counter()
counter()
counter()
counter()
counter()


