public List<TreeNode> kDistanceNodes(TreeNode root, TreeNode target, int k) {
    List<TreeNode> res = new ArrayList<>();
    kDistanceNodes(root, target, k, res);
    return res;
}

private int kDistanceNodes(TreeNode root, TreeNode target, int k, List<TreeNode> res) {
    if (root == null) {
        return -1;
    }
    if (root == target) {
        helperDown(target, k, res);
        return 0;
    }
    int dl = kDistanceNodes(root.left, target, k, res);
    if (dl != -1) {
        if (dl + 1 == k) {
            res.add(root);
        } else {
            helperDown(root.right, k - dl - 2, res);
        }
        return dl + 1;
    }
    int dr = kDistanceNodes(root.right, target, k, res);
    if (dr != -1) {
        if (dr + 1 == k) {
            res.add(root);
        } else {
            helperDown(root.left, k - dr - 2, res);
        }
        return dr + 1;
    }
    return -1;
}

private void helperDown(TreeNode target, int k, List<TreeNode> res) {
    if (target == null || k < 0) {
        return;
    }
    if (k == 0) {
        res.add(target);
    }
    helperDown(target.left, k - 1, res);
    helperDown(target.right, k - 1, res);
}
