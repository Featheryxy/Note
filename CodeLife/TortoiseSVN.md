## 简介

SVN全称Subversion，是⼀个开放源代码的版本控制系统，管理着随时间改变的数据。这些数据放置在⼀个中央资料档 案库(repository) 中。 这个档案库很像⼀个普通的⽂件服务器, 不过它会记住每⼀次⽂件的变动。 这样你 就可以把档案恢复到旧的版本, 或是浏览⽂件的变动历史。说得简单⼀点SVN就是⽤于多个⼈共同开发同 ⼀个项⽬，共⽤资源的⽬的。

## 基本概念

- Repository（源代码库）：源代码统⼀存放的地⽅
- Checkout（提取）：当你⼿上没有源代码的时候，你需要从repository checkout⼀份
- Commit（提交）：当你已经修改了代码，你就需要Commit到Repository
- Update (更新)：当你已经Checkout了⼀份源代码， Update后就可以和Repository上的源代码同步

## 生命周期

### 创建版本库 

版本库相当于⼀个集中的空间，⽤于存放开发者所有的⼯作成果。**版本库不仅能存放⽂件，还包括了每次修改的历史，即每个⽂件的变动历史。** **Create 操作是⽤来创建⼀个新的版本库。**⼤多数情况下这个操作只会执⾏⼀次。当你创建⼀个新的版本库的时候，你的版本控制系统会让你提供⼀些信息来标识版本库，例如创建的位置和版本库的名字。 

### 检出

 **Checkout 操作是⽤来从版本库创建⼀个⼯作副本。**⼯作副本是开发者私⼈的⼯作空间，可以进⾏内容 的修改，然后提交到版本库中。

### 更新 

顾名思义，**update 操作是⽤来更新版本库的**。这个操作**将⼯作副本与版本库进⾏同步**。由于版本库是 由整个团队共⽤的，当其他⼈提交了他们的改动之后，你的⼯作副本就会过期。 

让我们假设 Tom 和 Jerry 是⼀个项⽬的两个开发者。他们同时从版本库中检出了最新的版本并开始⼯ 作。此时，⼯作副本是与版本库完全同步的。然后，Jerry 很⾼效的完成了他的⼯作并提交了更改到版 本库中。 此时 Tom 的⼯作副本就过期了。更新操作将会从版本库中拉取 Jerry 的最新改动并将 Tom 的⼯作副本进⾏更新

### 执⾏变更 

当检出之后，你就可以做很多操作来执⾏变更。编辑是最常⽤的操作。你可以编辑已存在的⽂件来， 例如进⾏⽂件的添加/删除操作。 

你可以添加⽂件/⽬录。但是这些添加的⽂件⽬录不会⽴刻成为版本库的⼀部分，⽽是被添加进待变更 列表中，直到执⾏了 commit 操作后才会成为版本库的⼀部分。

同样地你可以删除⽂件/⽬录。删除操作⽴刻将⽂件从⼯作副本中删除掉，但该⽂件的实际删除只是被 添加到了待变更列表中，直到执⾏了 commit 操作后才会真正删除。 Rename 操作可以更改⽂件/⽬录的名字。"移动"操作⽤来将⽂件/⽬录从⼀处移动到版本库中的另⼀ 处。 

### 复查变化 

当你检出⼯作副本或者更新⼯作副本后，你的⼯作副本就跟版本库完全同步了。但是当你对⼯作副本 进⾏⼀些修改之后，你的⼯作副本会⽐版本库要新。在 commit 操作之前复查下你的修改是⼀个很好的习惯。 

**Status 操作**列出了⼯作副本中所进⾏的变动。正如我们之前提到的，你对⼯作副本的任何改动都会成 为待变更列表的⼀部分。Status 操作就是⽤来查看这个待变更列表。 

Status 操作只是提供了⼀个变动列表，但并不提供变动的详细信息。你可以⽤ diff 操作来查看这些变 动的详细信息。

### 修复错误 

我们来假设你对⼯作副本做了许多修改，但是现在你不想要这些修改了，这时候 revert 操作将会帮助你。 

**Revert 操作**重置了对⼯作副本的修改。它可以重置⼀个或多个⽂件/⽬录。当然它也可以重置整个⼯作 副本。在这种情况下，revert 操作将会销毁待变更列表并将⼯作副本恢复到原始状态。 

### 解决冲突 

合并的时候可能会发⽣冲突。Merge 操作会⾃动处理可以安全合并的东⻄。其它的会被当做冲突。例 如，"hello.c" ⽂件在⼀个分⽀上被修改，在另⼀个分⽀上被删除了。这种情况就需要⼈为处理。Resolve 操作就是⽤来帮助⽤户找出冲突并告诉版本库如何处理这些冲突。

### 提交更改 

**Commit 操作**是⽤来将更改从⼯作副本到版本库。这个操作会修改版本库的内容，其它开发者可以通 过更新他们的⼯作副本来查看这些修改。

 在提交之前，你必须将⽂件/⽬录添加到待变更列表中。列表中记录了将会被提交的改动。当提交的时 候，我们通常会提供⼀个注释来说明为什么会进⾏这些改动。这个注释也会成为版本库历史记录的⼀部 分。Commit 是⼀个原⼦操作，也就是说要么完全提交成功，要么失败回滚。⽤户不会看到成功提交⼀ 半的情况。
