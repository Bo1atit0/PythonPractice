// Filename: hello_cpython.c

#include <python.h>

int main(int argc, char *argv[]) {
    // Initialize the Python interpreter
    Py_Initialize();

    // Run a simple Python command
    PyRun_SimpleString("print('Hello from C using CPython!')");

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
