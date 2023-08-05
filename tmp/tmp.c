// 종목 코드를 저장할 자료구조...
// 종목 코드는 2000개 가량.
// 따로 저장하기엔 넘나 노가다.

// 1. trie -> O(36^6) -> eva
// 2. 

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ALPHABET_SIZE 26

struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    bool isEndOfWord;
};

struct TrieNode* createNode() {
    struct TrieNode* node = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        node->children[i] = NULL;
    }
    node->isEndOfWord = false;
    return node;
}

void insert(struct TrieNode* root, const char* word) {
    struct TrieNode* curr = root;
    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a';
        if (!curr->children[index]) {
            curr->children[index] = createNode();
        }
        curr = curr->children[index];
    }
    curr->isEndOfWord = true;
}

bool search(struct TrieNode* root, const char* word) {
    struct TrieNode* curr = root;
    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a';
        if (!curr->children[index]) {
            return false;
        }
        curr = curr->children[index];
    }
    return (curr != NULL && curr->isEndOfWord);
}

int main() {
    struct TrieNode* root = createNode();
    
    insert(root, "apple");
    insert(root, "banana");
    insert(root, "grape");
    
    printf("Searching for 'apple': %s\n", search(root, "apple") ? "Found" : "Not found");
    printf("Searching for 'orange': %s\n", search(root, "orange") ? "Found" : "Not found");
    
    return 0;
}
