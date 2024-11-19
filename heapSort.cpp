#include <stdio.h>

// 두 요소를 교환하는 함수
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 힙 구성 함수 (Max Heap으로 재구성)
void heapify(int arr[], int n, int i) {
    int largest = i;         // 루트 노드
    int left = 2 * i + 1;     // 왼쪽 자식 노드
    int right = 2 * i + 2;    // 오른쪽 자식 노드

    // 왼쪽 자식이 더 큰 경우
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // 오른쪽 자식이 더 큰 경우
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // 루트가 최대값이 아닌 경우 교환하고 재귀적으로 힙 구성
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// 힙 정렬 함수
void heapSort(int arr[], int n) {
    // 배열을 최대 힙으로 변환
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // 힙에서 요소를 하나씩 꺼내 정렬
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);  // 루트를 배열 끝으로 이동
        heapify(arr, i, 0);      // 남은 요소로 힙 재구성
    }
}

// 배열 출력 함수
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// 메인 함수
int main() {
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    heapSort(arr, n);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
