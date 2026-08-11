/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
    
        // 1. divide the list into half
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        } 

        // 2. reverse the order of the second half of the list
        ListNode* second = slow->next;
        ListNode* prev = slow->next = nullptr;
        while(second != nullptr){
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp; 
        }

        // 3. merge the first half and second (in reversed order)
        ListNode* first = head;
        second = prev;
        while(second != nullptr){
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }

        
    }
};
