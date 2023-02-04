public class Layer {
    private DoubleLinkedList members;
    private int depth;
    private Node father;

    public Layer(Node member) {
        this.members = new DoubleLinkedList(member, this);
        this.depth = 0;
    }

    public DoubleLinkedList getMembers() {
        return members;
    }

    public Node getFather() {
        return father;
    }

    public void setFather(Node father) {
        this.father = father;
        this.depth = father.getFamily().getDepth() + 1;
    }

    public int getDepth() {
        return depth;
    }

    public Layer add(Layer other) {
        if (other != null) {
            this.members = this.members.merge(other.members);
        }
        return this;
    }

    public void add(Node node) {
        this.members.addNode(node);
    }

    public void add(int key) {
        this.members.addNode(new Node(key, this));
    }


    public void updateDepth() {
        this.depth += 1;

    }

}
