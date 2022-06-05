import request from '@/utils/request'

export function dataTpyeList(params) {
  return request({
    url: '/api/datas/list',
    method: 'get',
    params
  })
}

export function getBaseData(data) {
  return request({
    url: '/api/datas/base',
    method: 'post',
    data
  })
}

export function getSceneData(data) {
  return request({
    url: '/api/datas/scene',
    method: 'post',
    data
  })
}
