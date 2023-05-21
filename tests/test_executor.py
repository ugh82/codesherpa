import pytest
import subprocess
from executors.executor import PythonExecutor, CppExecutor, RustExecutor

def test_python_executor():
    # Positive Case
    executor = PythonExecutor()
    code = "print('Hello, World!')"
    result = executor.execute(code)
    assert result == "Hello, World!\n"

    # Negative Case
    code = "print('Hello, World!'"
    with pytest.raises(subprocess.CalledProcessError):
        result = executor.execute(code)

def test_cpp_executor():
    # Positive Case
    executor = CppExecutor()
    code = """
    #include <iostream>
    int main() {
        std::cout << "Hello, World!" << std::endl;
        return 0;
    }
    """
    result = executor.execute(code)
    assert result == "Hello, World!\n"

    # Negative Case
    code = """
    #include <iostream>
    int main() {
        std::cout << "Hello, World!" << std::endl
        return 0;
    }
    """
    with pytest.raises(subprocess.CalledProcessError):
        result = executor.execute(code)

def test_rust_executor():
    # Positive Case
    executor = RustExecutor()
    code = """
    fn main() {
        println!("Hello, World!");
    }
    """
    result = executor.execute(code)
    assert result == "Hello, World!\n"

    # Negative Case
    code = """
    fn main() {
        println!("Hello, World!);
    }
    """
    with pytest.raises(subprocess.CalledProcessError):
        result = executor.execute(code)