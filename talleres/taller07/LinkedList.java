/**
 * Taller 7
 * 
 * LinkedList implementation in Java.
 * 
 * @author  Juan Pablo Vidal
 *          Alejandro Murillo
 */
public class LinkedList {
    
    /**
     * Execution of some test cases.
     * @param args 
     */
      public static void main(String args[]) {
          
          LinkedList list = new LinkedList();
          list.add(1);
          list.add(2);
          list.add(3);
          list.add(4);
          
          list.print();
          
          list.add(10);
          
          list.print();
          
          list.addAtStart(3);
          
          list.print();
          list.printInverse();
          try {
                list.print(3);
          } catch (Exception error) {
                System.out.println(error);
          }
          
          list.deleteEnd();
          list.print();
          
          list.deleteStart();
          list.print();
          
          try {
            System.out.println(maximum(list));
          } catch (Exception error) {
              System.out.println(error);
          }
          
          LinkedList list2 = new LinkedList();
          list2.add(3);
          list2.add(9);
          
          System.out.println(list.compareTo(list2));
      }
      
      /**
       * The first node of the LinkedList.
       */
      Node start;
      /**
       * LinkedList's size.
       */
      int size;
       
      /**
       * List Nodes.
       */
       private class Node {    
           int data;     
           Node next; 
           
           public Node(int data){    
               this.data = data;
           }
       }  
       
       /**
        * Creates a new LinkedList
        * and initializes the first
        * node to null.
        */
       public LinkedList(){ 
           start= null;
       } 
       
       /**
        * Adds an element at the start of 
        * the LinkedList.
        * @param n 
        */
       public void addAtStart(int n) {  
           Node newNode = new Node(n);
           
           if (start != null) {
               newNode.next = start; 
               start= newNode;      
           } 
           else { 
               start = newNode;
           }
           
           this.size += 1;
       }
       
       /**
        * Prints the elements of the list
        * on console.
        */
       public void print() {
           
           String elements = "[";
           
           Node n = this.start;
           while (n != null) { 
               elements += n.data +  ", ";
               n = n.next;
           }
           System.out.println(elements.substring(0, elements.length() - 2) + "]");
        } 
       
       /**
        * Adds an element to the end of the list.
        * 
        * @param n 
        */
       public void add(int n) {
           
           if (this.start == null) {
               this.start = new Node(n);
               return;
           }
                       
           Node node = this.start;
           while (node.next != null) {
               node = node.next;
           }
           node.next = new Node(n);
           this.size += 1;
       }
       
       /**
        * Prints the elements of the
        * list in reverse order.
        */
       public void printInverse() { 
           
           String elements = "";
           Node n = this.start;
           while (n != null) { 
               elements = ", " + n.data + elements;
               n = n.next;
           }
           System.out.println("[" + elements.substring(2) + "]");
           
       }
       
       /**
        * Prints the element at position n.
        * 
        * @param n
        * @throws Exception 
        */
       public void print(int n) throws Exception { 
           
           if (n >= size) {
               throw new Exception("Array Out of Bound Exception");
           }
           
           Node node = this.start;
           for (int i = 0; i < n && node != null; ++i) {
               node = node.next;
           }
           System.out.println(node.data);
       }  
       
       /**
        * Deletes the last element on
        * the LinkedList.
        */
       public void deleteEnd() { 
           
           Node node = this.start;
           while (node.next.next != null) {
               node = node.next;
           }
           node.next = null;
           this.size -= 1;
       }
       
       /**
        * Deletes the first element of the 
        * LinkedList.
        */
       public void deleteStart() { 
           
           this.start = this.start.next;
           this.size -= 1;
       }
       
       /**
        * Recursively search for the maximum
        * element.
        * 
        * @param node
        * @return 
        */
       private static int maximoAux(Node node) {
           if (node.next == null) return node.data;
           
           if (node.data > node.next.data)
               node.next.data = node.data;
           
           return maximoAux(node.next);
       }
       
       /**
        * Returns the maximum element of a
        * LinkedList.
        * 
        * @param lista
        * @return
        * @throws Exception 
        */
       public static int maximum(LinkedList lista) throws Exception {
           if (lista.start == null)
               throw new Exception("Null LinkedList: Behaviour undefined.");
           
           return maximoAux(lista.start);
       }
       
       /**
        * Compares this LinkedList with 
        * the one sent as a parameter.
        * If they are equal returns true,
        * false otherwise.
        * 
        * @param list
        * @return 
        */
       public boolean compareTo(LinkedList list) {  
           
           Node nodeThis = this.start;
           Node nodeThat = list.start;
           while (nodeThis != null) { 
               if (nodeThis.data != nodeThat.data || (nodeThis.next == null && nodeThat.next != null) || (nodeThat.next == null && nodeThis.next != null)) 
                   return false;
               nodeThis = nodeThis.next;
               nodeThat = nodeThat.next;        
           }
           
           return true;
       }  
}
