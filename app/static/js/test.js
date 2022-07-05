//$("#content").hide()
//console.log($("#content").text());
var init_content = $("#content").text();
console.log(init_content);

//使用before插入语句
$("#content").before("<div id='toolbar-container'></div><div id='editor-container'></div>")

const { createEditor, createToolbar } = window.wangEditor

// 编辑器配置
const editorConfig = { MENU_CONF: {} }
editorConfig.placeholder = '请输入内容'
editorConfig.onChange = (editor) => {
    document.getElementById('content').value = editor.getHtml()
}

editorConfig.MENU_CONF['uploadImage'] = {
     server: '/api/v1/uploadapi/upload_image',
     fieldName: 'image',
     maxFileSize: 30 * 1024 * 1024, // 1M
    // 上传之前触发
    onBeforeUpload(file) {
        return file
    }
}

// 工具栏配置
const toolbarConfig = {}

// 创建编辑器
const editor = createEditor({
  html: init_content,
  selector: '#editor-container',
  config: editorConfig,
  mode: 'default'// 或 'simple' 参考下文
})
// 创建工具栏
const toolbar = createToolbar({
  editor,
  selector: '#toolbar-container',
  config: toolbarConfig,
  mode: 'default' // 或 'simple' 参考下文
})

