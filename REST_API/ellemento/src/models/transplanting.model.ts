import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class Transplanting extends Entity {
  @property({
    type: 'number',
    required: true,
  })
  tray_action_table_id: number;

  @property({
    type: 'number',
    required: true,
  })
  tray_id: number;

  @property({
    type: 'number',
    required: true,
  })
  state_id: number;

  @property({
    type: 'number',
    required: true,
  })
  pre_action: number;

  @property({
    type: 'number',
    required: true,
  })
  post_action: number;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Transplanting>) {
    super(data);
  }
}

export interface TransplantingRelations {
  // describe navigational properties here
}

export type TransplantingWithRelations = Transplanting & TransplantingRelations;
