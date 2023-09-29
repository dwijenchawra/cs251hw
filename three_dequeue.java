import java.util.ArrayList;

class Dequeue {

    Stack frontStack;
    Stack backStack;
    Stack tempStack;

    class Stack {
        ArrayList<Integer> data;
        int top;

        Stack() {
            data = new ArrayList<>();
            top = -1;
        }

        void push(int val) {
            data.add(val);
            top++;
        }

        int pop() {
            if (top == -1) {
                System.out.println("Stack is empty");
                return -1;
            }
            int val = data.get(top);
            data.remove(top);
            top--;
            return val;
        }
    }

    Dequeue() {
        Stack frontStack = new Stack();
        Stack backStack = new Stack();
        Stack tempStack = new Stack();
    }

    void pushFront(int val) {
        frontStack.push(val);
    }

    void pushBack(int val) {
        backStack.push(val);
    }

    int popFront() {
        if (frontStack.top == -1) {
            if (backStack.top == -1) {
                System.out.println("Dequeue is empty");
                return -1;
            }
            while (backStack.top != -1) {
                tempStack.push(backStack.pop());
            }
            int val = tempStack.pop();
            while (tempStack.top != -1) {
                backStack.push(tempStack.pop());
            }
            return val;
        }
        return frontStack.pop();
    }






    public static void main(String[] args) {
        
    }
}
