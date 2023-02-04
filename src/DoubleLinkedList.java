
public class DoubleLinkedList {
    private Node min;
    private Node first;
    private Layer layer;

    public DoubleLinkedList(Node first, Layer layer) {
        this.min = first;
        this.first = first;
        this.layer = layer;
        this.first.addToFamily(layer);
    }

    public void addNode(Node other) {
        other.addToFamily(this.layer);
        if (min.getKey() > other.getKey()) {
            int key = other.getKey();
            other.setKey(min.getKey());
            min.setKey(key);
        }

        first.setPrevious(other);
        other.setNext(first);
        first = other;
    }


    public void print() {
        Node temp = first;
        while (temp.getNext() != null) {
            System.out.println(temp.getKey());
            temp = temp.getNext();
        }
        System.out.println(temp.getKey());
    }

    public Node getFirst(){
        return first;
    }

    public void setFirst(Node node){
        this.first=node;
    }

    public int getMin() {
        return min.getKey();
    }

    public void setMin(Node node){
        this.min=node;
    }

    public void moveMin() {
        min = min.getPrevious();
        min.getNext().exterminate();
    }
    public Node getLast(){ return min; }

    public DoubleLinkedList merge(DoubleLinkedList other) {
        if (this.getMin() > other.getMin()) {
            other.first.setPrevious(this.min);
            this.min.setNext(other.first);
            other.first = this.first;
            other.layer=this.layer;
            return other;
        } else {
            this.first.setPrevious(other.min);
            other.min.setNext(this.first);
            this.first = other.first;
            return this;
        }
    }

    public void pushToEnd(Node temp){
        if (temp.equals(first)){
            first = first.getNext();
        }
        temp.exterminate();
        min.setNext(temp);
        temp.setPrevious(min);
        min = temp;
    }

    public void pushToStart(Node temp){
        if (temp.equals(min)) {
            min = min.getPrevious();
        }
        temp.exterminate();
        first.setPrevious(temp);
        temp.setNext(first);
        first = temp;
    }
}



