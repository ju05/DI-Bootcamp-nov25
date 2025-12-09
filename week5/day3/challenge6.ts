interface SetManager<T> {
  addItem(item: T): void;
  clearAll(): void;
}

class SimpleSet<T> implements SetManager<T> {
  private items: T[] = [];

  addItem(o: T): void {
    this.items.push(o);
  }
  clearAll() {
    this.items = [];
  }
}
