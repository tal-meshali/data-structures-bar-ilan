public class main {
    public static void main(String[] args) {
        Root heap = new Root(3);
        heap.add(1);
        heap.add(4);
        heap.add(5);
        heap.add(7);
        heap.add(10);
        heap.add(8);
        heap.add(11);
        heap.add(6);
        heap.add(34);
        heap.add(12);
        heap.add(46);
        heap.add(25);
        heap.deleteMinimum();
        System.out.print(heap);
    }
}
