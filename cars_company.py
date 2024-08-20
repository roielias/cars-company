def create_node(license_plate, manufacturer, model, year):
    """
    Create a new tree node.

    :param license_plate: License plate of the vehicle.
    :param manufacturer: Manufacturer of the vehicle.
    :param model: Model of the vehicle.
    :param year: Year of the vehicle.
    :return: Dictionary representing the tree node.
    """
    return {
        "license_plate": license_plate,
        "manufacturer": manufacturer,
        "model": model,
        "year": year,
        "left": None,
        "right": None
    }

def insert(tree, license_plate, manufacturer, model, year):
    """
    Insert a new node into the binary search tree.

    :param tree: The root of the tree.
    :param license_plate: License plate of the vehicle.
    :param manufacturer: Manufacturer of the vehicle.
    :param model: Model of the vehicle.
    :param year: Year of the vehicle.
    :return: The updated tree.
    """
    if not tree:
        return create_node(license_plate, manufacturer, model, year)
    
    current = tree
    while True:
        if license_plate < current["license_plate"]:
            if current["left"] is None:
                current["left"] = create_node(license_plate, manufacturer, model, year)
                break
            else:
                current = current["left"]
        else:
            if current["right"] is None:
                current["right"] = create_node(license_plate, manufacturer, model, year)
                break
            else:
                current = current["right"]
    return tree

def search(tree, license_plate):
    """
    Search for a node with the given license plate.

    :param tree: The root of the tree.
    :param license_plate: License plate of the vehicle to search for.
    :return: The node with the matching license plate, or None if not found.
    """
    current = tree
    while current:
        if license_plate == current["license_plate"]:
            return current
        elif license_plate < current["license_plate"]:
            current = current["left"]
        else:
            current = current["right"]
    return None

def delete_1(tree, license_plate):
    """
    Public function to delete a node with the given license plate.

    :param tree: The root of the tree.
    :param license_plate: License plate of the vehicle to delete.
    :return: The updated tree.
    """
    return delete_2(tree, license_plate)

def delete_2(node, license_plate):
    """
    Recursively delete a node with the given license plate.

    :param node: The current node in the recursion.
    :param license_plate: License plate of the vehicle to delete.
    :return: The updated node.
    """
    if node is None:
        return node

    if license_plate < node["license_plate"]:
        node["left"] = delete_2(node["left"], license_plate)
    elif license_plate > node["license_plate"]:
        node["right"] = delete_2(node["right"], license_plate)
    else:
        if node["left"] is None:
            return node["right"]
        elif node["right"] is None:
            return node["left"]

        temp = node["right"]
        while temp["left"]:
            temp = temp["left"]

        node["license_plate"] = temp["license_plate"]
        node["manufacturer"] = temp["manufacturer"]
        node["model"] = temp["model"]
        node["year"] = temp["year"]

        node["right"] = delete_2(node["right"], temp["license_plate"])

    return node

def print_in_order(tree):
    """
    Print the nodes of the tree in in-order traversal.

    :param tree: The root of the tree.
    """
    if tree:
        print_in_order(tree["left"])
        print(f"License Plate: {tree['license_plate']}, Manufacturer: {tree['manufacturer']}, Model: {tree['model']}, Year: {tree['year']}")
        print_in_order(tree["right"])
