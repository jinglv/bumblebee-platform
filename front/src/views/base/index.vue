<template>
  <div class="data-base">
    <el-card style="height: 100%;">
      <div style="height: 50px">
        <span>基础数据类型：</span>
        <el-select v-model="dataBaseForm.dataName" placeholder="请选择..." @change="changeBaseData">
          <el-option
            v-for="item in dataBaseTypeOption"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>
      <div class="div-line" style="height: 150px">
        <el-input
          v-model="getBaseData"
          type="textarea"
          :rows="5"
          placeholder="生成的数据"
        />
      </div>
      <div style="height: 50px">
        <span>场景数据类型：</span>
        <el-select v-model="dataSceneForm.sceneName" placeholder="请选择..." @change="changeSceneData">
          <el-option
            v-for="item in dataBaseSceneOption"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>
      <div class="div-line" style="height: 350px">
        <el-input
          v-model="getSceneData"
          type="textarea"
          :rows="15"
          placeholder="生成的数据"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
import { dataTpyeList, getBaseData, getSceneData } from '@/api/datas'

export default {
  data() {
    return {
      dataBaseTypeOption: [],
      dataBaseSceneOption: [],
      getBaseData: '',
      getSceneData: '',
      dataBaseForm: {
        'dataName': ''
      },
      dataSceneForm: {
        'sceneName': ''
      },
      req: {
        page: 1,
        size: 6
      },
      // 分页页数
      total: 10
    }
  },
  mounted() {
    this.initDataTypeList()
  },
  methods: {
    // 初始数据类型列表
    async initDataTypeList() {
      const resp = await dataTpyeList(this.req)
      if (resp.success === true) {
        for (let i = 0; i < resp.items.length; i++) {
          if (resp.items[i].data_type === 'base') {
            this.dataBaseTypeOption.push({
              value: resp.items[i].data_name,
              label: resp.items[i].data_ch
            })
          } else if (resp.items[i].data_type === 'scene') {
            this.dataBaseSceneOption.push({
              value: resp.items[i].data_name,
              label: resp.items[i].data_ch
            })
          }
        }
        // this.$message.success("查询成功！")
      } else {
        this.$message.error('查询失败！')
      }
    },
    async getBaseDataInfo(dataForm) {
      const resp = await getBaseData(dataForm)
      if (resp.success === true) {
        this.getBaseData = JSON.stringify(resp.result, null, 2)
      }
    },
    async getSceneDataInfo(dataForm) {
      const resp = await getSceneData(dataForm)
      if (resp.success === true) {
        this.getSceneData = JSON.stringify(resp.result, null, 2)
      }
    },
    // 选中选项，生成对应的数据
    changeBaseData() {
      this.getBaseDataInfo(this.dataBaseForm)
    },
    changeSceneData() {
      this.getSceneDataInfo(this.dataSceneForm)
    }
  }
}
</script>
