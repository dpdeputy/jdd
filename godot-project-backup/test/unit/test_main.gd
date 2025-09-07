extends "res://addons/gut/test.gd"

var main_scene = load("res://scenes/main.tscn")

func test_label_text_is_hello_world():
    var main_instance = main_scene.instance()
    add_child_autofree(main_instance)

    var label = main_instance.get_node("Label")
    assert_eq(label.text, "Hello, World!", "Label text should be 'Hello, World!' after _ready")
