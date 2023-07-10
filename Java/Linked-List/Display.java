
class LinkedList {

    Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public static void insert(LinkedList list, int data) {

        Node new_node = new Node(data);
        new_node.next = null;

        if (list.head == null) {
            list.head = new_node;
        } else {

            Node last = list.head;
            while (last.next != null) {
                last = last.next;
            }

            last.next = new_node;
        }
    }

    public static void printList(LinkedList list) {

        Node currNode = list.head;

        System.out.print("LinkedList: ");

        while (currNode != null) {

            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }
    }

    public static void main(String[] args) {
        System.out.println("Hello World \n");

        LinkedList list = new LinkedList();

        insert(list, 90);

        printList(list);
    }
}