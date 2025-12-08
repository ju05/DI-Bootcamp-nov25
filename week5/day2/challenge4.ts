interface Mailable {
  send(email: string): boolean;
  queue(email: string): boolean;
}

interface ExtendedMailable extends Mailable {
  schedule(email: string, delay: number): void;
}

// Create an interface Shape with a method draw(). Create another interface Colorable with a method setColor(color: string). Extend both interfaces in a new interface called ColorableShape.

interface Shape {
  draw(): string;
}

interface Colorable {
  setColor(color: string): any;
}

interface ColorableShape extends Shape, Colorable {}
