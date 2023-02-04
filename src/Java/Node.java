public class Node {
    private int key;
    private boolean marked;
    private Node previous;
    private Node next;
    private Layer children;
    private Layer family;
    private int depth_of_children;

    public Node(int key, Layer family) {
        this.key = key;
        this.marked = false;
        this.family = family;
        this.depth_of_children = 0;
    }

    public Node(int key) {
        this.key = key;
        this.marked = false;
        this.depth_of_children = 0;
    }

    public Node getPrevious() {
        return previous;
    }

    public void setPrevious(Node previous) {
        this.previous = previous;
    }

    public void removePrevious() {
        this.previous = null;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public void removeNext() {
        this.next = null;
    }

    public int getKey() {
        return key;
    }

    public void setKey(int key) {
        this.key = key;
    }

    public void exterminate() {
        if (this.previous != null) {
            this.previous.setNext(this.next);
        } else {
            this.getFamily().getMembers().setFirst(this.getNext());
        }
        if (this.next != null) {
            this.next.setPrevious(this.previous);
        } else {
            this.getFamily().getMembers().setMin(this.getPrevious());
        }
        this.previous = null;
        this.next = null;
    }

    public void shiftMark() {
        this.marked = !this.marked;
    }

    public void adopt(Node other) {
        if (this.getKey() > other.getKey()) {
            this.exterminate();
            other.addChild(new Layer(this));
            this.addDepth();
        } else {
            other.exterminate();
            this.addChild(new Layer(other));
            other.addDepth();
        }
    }

    public void addChild(Layer child) {
        if (this.children == null) {
            this.children = child;
        } else {
            this.children.add(child);
        }
        child.setFather(this);
    }

    public void addToFamily(Layer family) {
        this.family = family;
    }

    public Layer getFamily() {
        return family;
    }

    public void setFamily(Layer family) {
        this.family = family;
    }

    public Layer getChildren() {
        return children;
    }

    public void removeChildren() {
        this.children = null;
    }

    public void removeFamily() {
        this.family = null;
    }

    public int getDepth() {
        return depth_of_children;
    }

    public void setDepth(int depth) {
        this.depth_of_children = depth;
    }

    public void addDepth() {
        if (this.getFamily().getFather() != null) {
            this.getFamily().getFather().setDepth(max(this.depth_of_children + 1, this.getFamily().getFather().getDepth()));
            this.getFamily().getFather().addDepth();
        }
    }

    public int max(int x1, int x2) {
        if (x1 > x2) {
            return x1;
        }
        return x2;
    }

    public boolean isMarked() {
        return marked;
    }
}
