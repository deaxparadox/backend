interface Calculate {
    default: string;
    setDefault(): void;

    valueA: string;
    valueB: string;
    operator: string;

    convertToNumber(value: string): number;
    add(values: {a: number, b: number}): void;
    pad1: string[][];
    numbers: string[];
    sequence: string[];

    click(e: any): void;
    get_number(value: string): void;
    get_operator(value: string): void;
    equal(value: string): void;
    clear(value: string): void;
}

class Calculator implements Calculate {
    default: string = "0";
    setDefault(): void {
        this.default = "0";
    }
    valueA: string = "0";
    valueB: string = "0";
    operator: string = "";

    convertToNumber(value: string) {
        return Number(value)
    }

    add(values: { a: number, b: number }) {
        return values.a + values.b
    }

    pad1: string[][] = [
        ['1', '2', '3', '+'],
        ['4', '5', '6', '*'],
        ['7', '8', '9', '-'],
        ['C', '0', '/', '='],
    ]

    numbers: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

    sequence: string[] = [];

    click(e: any) {
        let value = e.target.innerText;

        if (value in this.numbers) {
            this.get_number(value);
        } else if (value === "=") {
            this.equal(value);
        } else if (value === "C") {
            this.clear(value);
        } else {
            this.get_operator(value);
        }
    }

    get_number(value: string) {
        if (this.operator) {
            this.valueA = "0";
            // this.valueB = this.valueB + value;
            // console.log(this.valueB)

        }

        this.valueA = this.valueA + value;
        console.log(this.valueA)

    }
    get_operator(value: string) {

        this.sequence.push(this.valueA);
        this.valueA = "0";

        this.operator = value;
        this.sequence.push(this.operator);
        console.log(this.sequence);
        // console.log(`Operator ${this.operator}`);

    }
    equal(value: string) {

        console.log("Pressed equal")

    }
    clear(value: string) {

        console.log("Cleared")

    }
}

export default Calculator;