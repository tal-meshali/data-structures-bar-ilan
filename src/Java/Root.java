public class Root extends Layer {

    private final Node[] degreesTable;

    public Root(int member) {
        super(new Node(member));
        this.degreesTable = new Node[20];
        this.getMembers().getFirst().setFamily(this);
    }

    public void deleteMinimum() {
        if (this.getDepth() == 0) {
            int minimum = this.getMembers().getMin();
            Layer addition = this.getMembers().getLast().getChildren();
            this.getMembers().moveMin();
            add(addition);
            while (true) {
                int degree = this.getMembers().getFirst().getDepth();
                // If there have already been found a different one, we go to the end, find the second of the same degree and merge them.
                if (degreesTable[degree] != null) {
                    if (!degreesTable[degree].equals(this.getMembers().getFirst())) {
                        Node temp = this.getMembers().getLast();
                        while (temp.getDepth() != degree) {
                            temp = temp.getPrevious();
                        }
                        this.getMembers().pushToStart(temp);
                        this.getMembers().getFirst().getNext().adopt(temp);
                        degreesTable[degree] = null;
                    } else {
                        break;
                    }
                }
                // If there is only one more tree left there is nothing to search for.
                else if (this.getMembers().getFirst().getPrevious() == null && this.getMembers().getFirst().getNext() == null) {
                    break;
                }
                // If there hasn't been found a subtree with that particular degree.
                else if (degreesTable[degree] == null) {
                    degreesTable[degree] = this.getMembers().getFirst();
                    this.getMembers().pushToEnd(this.getMembers().getFirst());
                }
                // If the first is also the only one of that same degree, then we stop the process.
                else {
                    break;
                }
            }
            Node temp = this.getMembers().getFirst();
            Node min = temp;
            if (!(this.getMembers().getFirst().getPrevious() == null && this.getMembers().getFirst().getNext() == null)) {
                while (temp.getNext() != null) {
                    if (temp.getKey() < min.getKey()) {
                        min = temp;
                    }
                    temp = temp.getNext();
                }
                this.getMembers().pushToEnd(min);
            }
        }
    }

    public void decreaseValue(Node node, int value) {
        node.setKey(value);
        removeNode(node);
        if (value < this.getMembers().getMin()) {
            this.getMembers().setMin(node);
        }
    }

    public void deleteNode(Node node) {
        node.setKey(-100000);
        removeNode(node);
        this.getMembers().setMin(node);
        deleteMinimum();
    }

    public void removeNode(Node node) {
        Node father = node.getFamily().getFather();
        if (node.getPrevious() == null && node.getNext() == null) {
            father.removeChildren();
            father.setDepth(0);
            node.removeFamily();
        } else {
            node.exterminate();
        }
        add(node);
        if (father.getFamily().getFather() != null) {
            if (father.isMarked()) {
                removeNode(father);
            } else {
                father.shiftMark();
            }
        }
    }
}
