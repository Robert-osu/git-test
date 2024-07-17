var createHelloWorld = function() {

	return function(...args) {
		const str = "Hello World";
		console.log(str);
	}
};
const f = createHelloWorld();
f({}, null, 42);
