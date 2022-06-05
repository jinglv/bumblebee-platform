<template>
  <el-dialog
    :title="showTitle"
    :visible.sync="dialogVisible"
    width="500px"
    :before-close="closeDialog"
  >
    <el-form
      ref="ruleForm"
      :model="projectForm"
      :rules="rules"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="项目名称" prop="name">
        <el-input v-model="projectForm.name" />
      </el-form-item>
      <el-form-item label="项目描述" prop="desc">
        <el-input v-model="projectForm.describe" type="textarea" />
      </el-form-item>
      <el-form-item label="图片" prop="desc">
        <div id="image">
          <el-upload
            action="#"
            :before-upload="beforeUpload"
            list-type="picture-card"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :file-list="fileList"
          >
            <i class="el-icon-plus" />
          </el-upload>
          <el-dialog :visible.sync="imageVisible">
            <img width="100%" :src="imageUrl" alt="">
          </el-dialog>
        </div>
      </el-form-item>
      <el-form-item style="text-align: right">
        <el-button @click="closeDialog">取消</el-button>
        <el-button
          type="primary"
          @click="submitForm('ruleForm')"
        >确定</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>
<script>
import { getProject } from '@/api/projects'

export default {
  name: 'PorjectDialog',
  components: {},
  // eslint-disable-next-line vue/require-prop-types
  props: ['title', 'pid'],
  data() {
    return {
      dialogVisible: true,
      showTitle: '',
      updateURL: '',
      projectForm: {
        name: '',
        describe: '',
        image: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入项目的名称', trigger: 'blur' }
        ]
      },
      fileList: [], // 现有图片列表
      imageUrl: '', // 图片路径
      imageVisible: false,
      disabled: false
    }
  },
  mounted() {
    if (this.title === 'create') {
      this.showTitle = '创建项目'
    } else if (this.title === 'edit') {
      this.showTitle = '编辑项目'
      this.initProjectDetail()
    }
  },
  methods: {
    closeDialog() {
      console.log('closeDialog')
      this.$emit('cancel', {})
    },
    // 查询项目详情
    async initProjectDetail() {
      const resp = await getProject(this.pid)
      if (resp.success === true) {
        this.projectForm = resp.result
        this.fileList.push({
          name: resp.result.image,
          url: 'static/images' + resp.result.image
        })
        this.$message.success('项目详情成功！')
      } else {
        this.$message.error('项目详情失败！')
      }
    }
  }
}
</script>
